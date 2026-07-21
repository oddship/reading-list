package main

import (
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "sort"
    "strings"
)

type pair struct {
    Tag   string
    Count int
}

var allowed = map[string]bool{
    "agents":          true,
    "ai-infra":        true,
    "developer-tools": true,
    "llm-research":    true,
    "org-design":      true,
    "security":        true,
    "systems":         true,
    "other":           true,
}

func main() {
    root := "."
    if len(os.Args) > 1 {
        root = os.Args[1]
    }

    counts := map[string]int{}
    invalid := map[string][]string{}
    tagRe := regexp.MustCompile(`(?m)^tags = \[(.*?)\]$`)
    dirs := []string{filepath.Join(root, "content", "notes"), filepath.Join(root, "content", "digests")}

    for _, dir := range dirs {
        filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {
            if err != nil || info.IsDir() || !strings.HasSuffix(path, ".md") {
                return nil
            }
            b, err := os.ReadFile(path)
            if err != nil {
                return nil
            }
            m := tagRe.FindStringSubmatch(string(b))
            if len(m) < 2 {
                return nil
            }
            raw := strings.Split(m[1], ",")
            for _, r := range raw {
                t := strings.Trim(strings.TrimSpace(r), `"`)
                if t == "" {
                    continue
                }
                counts[t]++
                if !allowed[t] {
                    invalid[t] = append(invalid[t], path)
                }
            }
            return nil
        })
    }

    rows := make([]pair, 0, len(counts))
    for k, v := range counts {
        rows = append(rows, pair{k, v})
    }
    sort.Slice(rows, func(i, j int) bool {
        if rows[i].Count == rows[j].Count {
            return rows[i].Tag < rows[j].Tag
        }
        return rows[i].Count > rows[j].Count
    })
    for _, row := range rows {
        fmt.Printf("%3d  %s\n", row.Count, row.Tag)
    }

    if counts["other"] > 20 {
        invalid["other-threshold"] = []string{fmt.Sprintf("other has %d notes; audit and refile or create a reusable new tag", counts["other"])}
    }

    if len(invalid) > 0 {
        keys := make([]string, 0, len(invalid))
        for k := range invalid {
            keys = append(keys, k)
        }
        sort.Strings(keys)
        fmt.Fprintln(os.Stderr, "\ninvalid public tags:")
        for _, k := range keys {
            fmt.Fprintf(os.Stderr, "- %s (%d files)\n", k, len(invalid[k]))
        }
        os.Exit(1)
    }
}

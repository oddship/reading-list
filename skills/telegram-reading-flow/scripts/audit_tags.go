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

func main() {
    root := "."
    if len(os.Args) > 1 {
        root = os.Args[1]
    }
    notesDir := filepath.Join(root, "content", "notes")
    tagRe := regexp.MustCompile(`(?m)^tags = \[(.*?)\]$`)
    counts := map[string]int{}
    filepath.Walk(notesDir, func(path string, info os.FileInfo, err error) error {
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
            if t != "" {
                counts[t]++
            }
        }
        return nil
    })
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
}

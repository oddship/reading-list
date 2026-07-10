package main

import (
    "bufio"
    "fmt"
    "os"
    "path/filepath"
    "regexp"
    "strings"
)

func fail(msg string) {
    fmt.Fprintln(os.Stderr, msg)
    os.Exit(1)
}

func main() {
    if len(os.Args) != 2 {
        fail("usage: go run skills/agent-skills-authoring/scripts/validate_skill.go <skill-dir>")
    }
    dir := os.Args[1]
    skillPath := filepath.Join(dir, "SKILL.md")
    b, err := os.ReadFile(skillPath)
    if err != nil {
        fail(err.Error())
    }
    text := string(b)
    if !strings.HasPrefix(text, "---\n") {
        fail("SKILL.md must start with YAML frontmatter")
    }
    parts := strings.SplitN(text[4:], "\n---\n", 2)
    if len(parts) != 2 {
        fail("SKILL.md must close frontmatter with ---")
    }
    fm := parts[0]
    body := strings.TrimSpace(parts[1])
    if body == "" {
        fail("SKILL.md body is empty")
    }
    nameRe := regexp.MustCompile(`(?m)^name:\s*([a-z0-9-]+)\s*$`)
    descRe := regexp.MustCompile(`(?m)^description:\s*(.+)$`)
    if !nameRe.MatchString(fm) {
        fail("missing or invalid name field")
    }
    if !descRe.MatchString(fm) {
        fail("missing description field")
    }
    skillName := nameRe.FindStringSubmatch(fm)[1]
    if len(skillName) > 64 {
        fail("name exceeds 64 chars")
    }
    desc := strings.TrimSpace(descRe.FindStringSubmatch(fm)[1])
    desc = strings.Trim(desc, `"'`)
    if len(desc) == 0 || len(desc) > 1024 {
        fail("description must be 1..1024 chars")
    }

    refs := map[string]bool{}
    scanner := bufio.NewScanner(strings.NewReader(body))
    for scanner.Scan() {
        line := scanner.Text()
        for _, prefix := range []string{"references/", "scripts/", "assets/"} {
            idx := strings.Index(line, prefix)
            if idx != -1 {
                path := strings.Fields(line[idx:])[0]
                path = strings.Trim(path, "`.,:)\"")
                refs[path] = true
            }
        }
    }
    for rel := range refs {
        full := filepath.Join(dir, rel)
        if _, err := os.Stat(full); err != nil {
            fail(fmt.Sprintf("referenced path missing: %s", rel))
        }
    }
    fmt.Printf("OK %s\n", skillName)
}

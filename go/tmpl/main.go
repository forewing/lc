package main

import (
	"fmt"
	"os"
	"path"
	"text/template"
)

// TemplateData holds data
type TemplateData struct {
	Problem string
}

func main() {

	if len(os.Args) < 2 {
		fmt.Println("Usage: go run ./tmpl PROBLEM")
		os.Exit(1)
	}

	t, err := template.ParseGlob("tmpl/*.tmpl")
	if err != nil {
		panic(err)
	}

	data := TemplateData{
		Problem: os.Args[1],
	}

	target := fmt.Sprintf("p%v", os.Args[1])

	err = os.MkdirAll(target, 0755)
	if err != nil {
		panic(err)
	}

	solutionWriter, err := os.Create(path.Join(target, target+".go"))
	if err != nil {
		panic(err)
	}
	testWriter, err := os.Create(path.Join(target, target+"_test.go"))
	if err != nil {
		panic(err)
	}

	t.ExecuteTemplate(solutionWriter, "solution.tmpl", data)
	t.ExecuteTemplate(testWriter, "test.tmpl", data)
}

package main

import (
	"sort"
	"strings"
)

type FileSystem struct {
	isDir    bool
	children map[string]*FileSystem
	content  string
	name     string
}

func Constructor() FileSystem {
	return FileSystem{
		isDir:    true,
		children: make(map[string]*FileSystem),
	}
}

func (fs *FileSystem) lookup(path string) *FileSystem {
	result := fs
	if path == "/" {
		return result
	}

	for _, name := range strings.Split(path, "/")[1:] {
		if result == nil {
			return result
		}
		result = result.children[name]
	}
	return result
}

func (fs *FileSystem) Ls(path string) []string {
	entry := fs.lookup(path)
	if !entry.isDir {
		return []string{entry.name}
	}
	children := []string{}
	for c := range entry.children {
		children = append(children, c)
	}
	sort.Strings(children)
	return children
}

func (fs *FileSystem) Mkdir(path string) {
	if fs.lookup(path) != nil {
		return
	}

	cur := fs
	for _, name := range strings.Split(path, "/")[1:] {
		next, ok := cur.children[name]
		if !ok {
			next = &FileSystem{
				isDir:    true,
				children: make(map[string]*FileSystem),
			}
			cur.children[name] = next
		}
		cur = next
	}
}

func (fs *FileSystem) AddContentToFile(filePath string, content string) {
	if file := fs.lookup(filePath); file != nil {
		file.content += content
		return
	}
	dir := fs
	names := strings.Split(filePath, "/")
	if len(names) > 2 {
		dirPath := strings.Join(names[:len(names)-1], "/")
		fs.Mkdir(dirPath)
		dir = fs.lookup(dirPath)
	}
	fileName := names[len(names)-1]
	file, ok := dir.children[fileName]
	if !ok {
		file = &FileSystem{
			isDir: false,
			name:  fileName,
		}
		dir.children[fileName] = file
	}
	file.content += content
}

func (fs *FileSystem) ReadContentFromFile(filePath string) string {
	return fs.lookup(filePath).content
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Ls(path);
 * obj.Mkdir(path);
 * obj.AddContentToFile(filePath,content);
 * param_4 := obj.ReadContentFromFile(filePath);
 */

func main() {
	fileSystem := Constructor()
	fileSystem.Ls("/") // return []
	fileSystem.Mkdir("/a/b/c")
	fileSystem.AddContentToFile("/a/b/c/d", "hello")
	fileSystem.Ls("/")                         // return ["a"]
	fileSystem.ReadContentFromFile("/a/b/c/d") // return "hello"
}

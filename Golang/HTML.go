package main
import . "fmt"

func main() {
    var myHtml = Html {
        head: Head {
            title: "My first Webpage",
        },
        body: Body {
            H1 { "Hello World!!" },
            Para { 
                "This is my 1st Webpage",
            },
        },
    };
    
    Print(myHtml.String())
}


type Html struct {
    head Head
    body Body
}


type Head struct {
    title string
    // meta []Meta
    // link []Link
    // base []Base
    // script Script
    // style Style
}


type Body []BodyElement


type BodyElement interface {
    BodyContent() string
}


type H1 struct { text string }


type Para struct { 
    text string 
    // children []BodyElement
}


func (this Html) String() string {
    return Sprintf("<!DOCTYPE html>\n"+
                   "<html>\n%s%s</html>",
                   this.head.String(),
                   this.body.String());
}


func (this Head) String() string {
    return Sprintf(" <head>\n  <title>%s"+
                   "</title>\n </head>\n",
                   this.title);
}


func (this Body) String() (content string) {
    content = " <body>\n"
    for _, elem := range this {
        content += Sprintf("  %s\n", 
                           elem.BodyContent());
    }
    content += " </body>\n"
    return
}


func (this H1) BodyContent() string {
    return Sprintf("<h1>%s</h1>", this.text)
}


func (this Para) BodyContent() string {
    return Sprintf("<p>%s</p>", this.text)
}

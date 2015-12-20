# Udacity - Intro To Programming Nanodegree
## The Basics of the Web and HTML

### Introduction to the Web
#### The Web
* WWW is a collection of hyperlinked HTML (HyperText Markup Language) documents.
* The major pieces of the web are you, your computer & browser, the internet and
 servers.
* Computer uses protocol HTTP to talk to the servers.

#### HTML
* HTML docs are the heart of the web, which is made up of text content, markup -
 what it looks like, references to other documents, and links to other pages.

#### Markup
* Markup is made up of tags, which look like this '<TAG-NAME>CONTENTS</TAG-NAME>
', this is an element.
* The <b> tag makes the content bold.
* The <em> tag makes content italic, it stands for emphasis.
* Computers are **stupid** in the sense that they will only ever do exactly what they are told to do by a human (although this gets a little less clear with machine learning and AI!).

#### Attributes
* Tags can contain attributes which can have a value, it look like this, '<TAG ATTR="VALUE">CONTENTS</TAG>'.
* Tags can have multiple attributes.
* The anchor tag '<a>' are for making links and have the attribute 'href="LINK"', eg. <a href="LINK">CONTENTS</a>.
* <img> is a tag for including images and has two attributes, 'src="url"' and 'alt="text"', alt identifies the text that gets displayed if the src url is broken. Img tags do not have a closing tag because it doesn't have any content, it is a 'void tag'.
* Whitespace in HTML are all turned into a single space, this includes multiple spaces or enters, these will be converted into a single space upon rendering.
* The <br> tag can be used to add line breaks into HTML. The <br> tag is also a void tag. <br> tags are inline.
* The <p> tag can be used to provide line breaks, these tags create paragraphs. <p> tags are block, which creates an invisible box around the content which can have it's own attributes like hight and width.

#### Container tags
* All these do is contain the content in them and can be used to add style to content.
* <span></span> is inline.
* <div></div> is block.

#### HTML documents
* A complete HTML document contains many different elements, including:
  * <!DOCTYPE HTML> - defines what kind of html the document is.
  * <HTML> - Surrounds the entrie document
  * <head> - Contains metadata and other scripts like, CSS and Javascrip     37 t
  * <title> - The title of the page or the URL
  * <body> - Everything you actually see on the webpage.

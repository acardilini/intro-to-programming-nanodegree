# Udacity - Intro To Programming Nanodegree
## Stage 1 Notes
---
### 1.2 Creating a Structured Document
This section will focus on how a HTML document is structured and how web
browsers interpret that structure. It will also go through the purpose of HTML,
CSS and javascript.

Why start learning programming with front-end web development? Understanding
front end web dev is one of the few areas of programming that is visual, which
allows new students to immediately see the effects of their programming. This is
a good feedback mechanism for beginner programmers who are just starting to learn.
It's also a easy way to share what you are creating, which allows you to show
off your skills to others easily.

#### What we will do
* Learn how to translate basic webpage design mockup to HTML and CSS in order
to create a webpage.
* Develop a CSS framework for creating fast and easy websites.
* Learn about responsive design to create webpages for any device.
* Build a static website using twitters bootstrap framework.

#### The First Step
Having a conceptual understanding of how the different components of a webpage
work will help translate visual designs into webpages. So HTML can be thought
of as the structure of the page, telling you where things go, whereas CSS defines
the style of the house, such as the colouring and decoration, and finally
javascript is the interactive element, allowing you to interact with the webpage
and cause a change. It's important to acknowledge that there are rules that
govern how websites behave.

#### Exploring the Web
Many web browsers have development tools that allow you to inspect the structure
and underlying code that makes up a webpage. In google chrome you can use it
by right clicking anywhere on a webpage and selecting 'inspect'. There are some
observable elements that are not visible on the page, such as the head tag.

#### Page Structure
Browsers build a branching tree-like structure of the page, which represents the
association between different elements. It is possible to draw a representation
of each element within a webpage using a simple branching structure, which can help
understanding the structure of a webpage. The tree structure is how HTML classifies
each element.

#### HTML-CSS-DOM
HTML is the language of the web with a specific syntax and rules. You write HTML
in a document following the syntax and rules of the language. The basic word in
the HTML language is 'tag', which browsers turn into elements that form a tree
(or DOM). The Document Object Model is a standard convention of representing and
interacting with HTML tags, and the tree that is seen in a browsers dev tool is
actually a DOM. Each HTML tag creates an element in the DOM which the browser
uses to create the webpage. The tag name defines what type of element is created,
tags can also provide attributes which define elements. As previously stated the
HTML defines the structure and content of the page, while the CSS language is
used to define the style of the elements and the page. CSS is a different language
with a different set of syntax and rules. The HTML document identifies what CSS
style to use and where to find the stylesheet. Once you understand both HTML and
CSS languages it is easier to look at a page and see how it can be broken down
into it's different elements, or vice versa, build a page up.

#### Boxes Everywhere
Every element on a webpage is a box, even circles are boxes! CSS can be used
to style elements, such as coloured boxes, and make the look like circles, e.g.
'border-radius'. However, they element is still fundamentally a box, its just
that it's style has been changed.

#### Boxes, Grids and Rules
Thinking about the elements of a website in terms of boxes makes it simple to
organise and rearrange the webpage. It allows you to think about a webpage in
terms of a grid, and identify where each element will be placed within that grid.

#### Boxifying Design
When you are given a mock design, it can helpful to boxify the design by drawing
boxes around the different elements you have identified.

#### Interview with Jacques
* Everything on the web is boxes, so starts with cutting the design into boxes.
Start with big and move through to small.
* Starts by recognising the boxes and worries about the content later. Just wants
to get the structure down first. Again starts with big boxes and works into the
smaller boxes after the big ones are identified.

#### Text Editor
It was suggested that the text editor Sublime Text 2 be downloaded and used,
however, I already have Atom and will see how I go using it.

#### Boxes to HTML
Boxes are defined by &lt;div&gt; tags. When creating a new webpage, start by
setting up all of the boxes/div tags you need. Once this is done you will wants
to be able to apply style to them, e.g. size and location, and the easiest way
to do this is to give each element a class attribute which distinguishes it's
purpose. CSS can then be used to style each of the different divs depending on
the class. It's important to make each class attribute meaningful to the div that
it identifies so that you recognise what it is at a later date.

### Work Session 1
Summarise my notes on section 1.2 and add them to my previous notes from stage0.

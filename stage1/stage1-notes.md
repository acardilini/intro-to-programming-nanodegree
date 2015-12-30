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

---
### 1.3 Adding CSS Style and HTML Structure
Learn how to add CSS code to add style to the webpage, and how to avoiding
repetition is key to good programming.

#### Adding Style
When no CSS style is included in the HTML document, the browser will default to
a standard 'boring' style. We include style the HTML by linking it to a CSS
file with the &lt;link rel="stylesheet type="text/css" href="LINK"&gt; tag,
which should be placed between the &lt;head&gt; tags.

Once the HTML and CSS files are linked you can use the CSS file to add style to
the HTML. For instance to make the description text red we use the following CSS
code:
```CSS
.description{
  color: red;
}
```
An alternative way to add style to HTML elements is by including
&lt;style&gt; tags in the &lt;head&gt; of the HTML document. However it is
generally better practice to creat a CSS file because it can be used to link to
many pages at once and cuts down repetition between webpages. For instance,
rather than having to change the style between &lt;style&gt; tags in multiple
webpages, you only have to change it once in a single CSS file that is linked
to all of the pages.

#### Understanding CSS
CSS stands for Cascading Style Sheets. Multiple CSS can be linked to a single
HTML document, with the most specific rules being applying the style
to the webpage. That is, there can be multple rules which govern how an
element should be styled but it is the **most specific** rule that
**is** applied. An [Inheritance](https://en.wikipedia.org/wiki/Cascading_Style_Sheets#Inheritance)
mechanisms that helps determine what styling is applied to elements of
a HTML document. It means that descendants of an element, i.e. tags
nested in other tags, will inherit the style of their ancestor elements.
The inheritance mechanism relies on the tree-like structure of the DOM
to determine styling for descendants. As previously stated, style applied directly to
a descendant overrides the style inherited from an ancestor, e.g. the
**most specific** rule is applied.

#### Style Up
CSS starts with a selector, which identifies what elements to apply
the style to. Selectors can be tag names, and will apply to all elements
of that tag, or can be more specific and target elements of a specific
class. CSS syntax follows the following simple structure:
```CSS
SELECTOR {
  ATTRIBUTE: VALUE;
}
```
CSS-Tricks (which is a great website and youtube channel), provides a good
introduction to [CSS-Selectors}(https://css-tricks.com/how-css-selectors-work/)
which is well worth checking out. There are also LOTS of different
attributes that can be specified to style HTML elements. Mozilla has
a [CSS reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
page that provide information about lots of these attributes and the
values that can be applied to them. It is important to note that there
are often several ways of defining the value of an attribute.

#### Understanding the Importance of Style
These are notes taken while watching a video conversation between Luke
and Mark. They are talking about how to properly style your written code
to make it easy to read HTML and CSS.
##### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; HTML
* It is important to provide good documentation, in order to communicate
to other people and your future self what you have done and why.
* Comments help people following along in your code and make it readable using indentation.
* Use a code text editor, it helps setting out correct coding style.
* Good code writing style helps you write more efficient code,
which helps you understand the code more efficiently. It also helps
with communication between coders.
* Clean, consistent and logical indentation goes a long way!
* In python there is a strong recommendation to only include 80 characters
per line.
* The &lt;pre&gt; tag can be used in HTML to include preformatted coding
for languages like python. In contrast the &lt;code&gt; tag doesn't
preserve the formatting, e.g. spaces, between the tags.
* Always use double quotes in HTML around attribute values, this helps with
integrating with other coding languages which you can use single quotes in.
* use lower case names when defining class or id attributes, and the names of the attributes.
* Add comments at the end of a large element, e.g. div, to indicate
where it ends. This can help you find things better.
##### CSS
* Be consistent with the placement of {}.
* Only have one attribute and value pair on each line.
* Use comments sparingly, use it to note the code that relates to
specific sections of your webpage. Try to keep them to one or two
sentences max. Use a 'TODO:' starter to make a comment about work you
need to do in the future.
* Add comments on how your doing what your doing or most importantly,
why you are doing what you are doing.
##### Python
* Indentation is not optional, it is necessary for the code to run.
* Give variables a sensible name that contextualises what it is and what you
are trying to do.

#### The Box Revisited
The box model which describes how every element box on a webpage is set
up includes a margin, border, padding and content. Each of the components
of the box model play a specific role in providing style to your elements:
* Content: Is the image or text that is appearing on the website, it sits
at the centre of your elements box. The other parts of the box 'protect'
the content so that other webpage elements don't sit to close or obscure
it.
* Padding: This clears the area around the content and is effected by the background color of the box.
* Border: This goes around the content and padding of the box.
* Margin: This clears an area around the boarder and is completely transparent.

By default the size of an element is equal to the sum of the box component
pixels. This can make it hard to know how much space the box will take up
on the screen especially if you are changing elements often. A simpler
model has been developed with this in mind and should be used:
```CSS
* {
  box-sizing: border-box;
}
```
This calculates the element size inlcuding both the border and padding.
It means you can set the over box size and tweaking the padding and border
will not change it. Margin is not included in this size, and there is a drawback to using it. It's relatively new and for some of the older browsers to use it special prefixes must be included, e.g.:
```CSS
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  -ms-box-sizing: border-box;
  box-sizing: border-box;
}
```
It is also possible to set box sizes as percentages rather than pixels. This can be helpful for creating responsive webpages. A max width can also be set for a box which means it will never get larger than the specified size, but will still get small when necessary.

#### Position Boxes
This is possibly one of the most complicated concepts in CSS,
and there are many different methods. We will be using the flexbox layout method,
which provides a flexible way for describing the layout of the webpage.
Styling a container/parent div with 'display: flex;' makes the items/child elements
try to align with one another. For this to work, the elements must also be
given a size the is less than 100%, for obvious reasons. CSS-Tricks
provides a [great description](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)
of flexbox use. Some attributes that are important when using flexbox include:
* For the container;
  * flex-direction
  * flex-wrap
  * flex-flow
  * justify-content
  * align-items
  * align-content
* flex-direction
  * order
  * flex-grow
  * flex-shrink
  * flex-basis
  * flex
  * align-self

#### Code, Test, Refine
The Code, Test and Refine routine is a good way to work towards creating
a design you have been given. A good place to start this process is to:
1. Boxifying the design.
2. Look for repeated style and symatic elements, i.e. figure out what tags are required.
3. Write the HTML.
4. Apply style, from the biggest to smallest elements.
5. Fix things. Look at the site in different browsers and repeat
steps 3 & 4 until the webpage looks like the design mock.

#### More on DevTools
Using browser DevTools can be helpful for making changes on the fly and quickly testing ideas.

#### Verifying HTML and CSS
It is important that you validate your code to check that it will work on
all of the different browsers available. Online tools help check [HTML](https://validator.w3.org/#validate_by_input)
and [CSS](http://jigsaw.w3.org/css-validator/#validate_by_input).
These methods provide validation icons that can be added to your website
to show that it meets appropriate standards.

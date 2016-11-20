# Udacity - Intro To Programming Nanodegree
## Stage 5 Notes
---
### 5.2 Lesson 0

#### The Resumes HTML
Web developers have two options, they can hard program a HTML page or they can can use an HTML template and fill it in with data programmatically upon user request.

A template strategy is much better for long term and d

The HTML header element includes script elements that point to the required JavaScript code.

#### CSS and JS in the Resume
JQuery is a JavaScript library that lets you inspect and manipulate elements within a HTML document.

#### Developer Tools
All modern browsers include developer tools that let you inspect various aspects of a website.

The console tool allows you to run basic commands, e.g. console.log(); which is the basic print command for JavaScript. console.log(); is particularly useful for debugging. It's important to remember to include the semi-colon ';' after code in JavaScript.

When console.log(); returns undefined it means that it hasn't created any new data that could be saved. This is good for debugging.

The console can also be used to manipulate local versions of webpages.

#### .append()
JQueries .append() function can be used to add HTML to an element on a page. If the element already has content append will add the new content to the end of the old content.

For example, using the stage5 documents if we wanted to add HTML to the`id="header"` element then we can use the following code. This includes the JQuery selector:
```javascript
$("#header").append([Adam Cardilini])
```

#### Summary
What technologies and techniques have we talked about so far?


* We have spoken about the different coding languages that will be used to create a dynamic resume. These include HTML, CSS and JavaScript, with learning how to use basic javascript being the main focus of these lessons.
* We will be using functions from the javascript package JQuery, and how these tools let us manipulate data in relation to the elements of an HTML page.
* We have spoken about developer tools and briefly explored how these can be used to manipulate website.
* We have touched on the use of console.log for debugging our code.
* We have discussed the use of .append() for adding information to an element of a HTML page.

### Lesson 1 - Data Types
#### Variables
JavaScript saves data in variables. To declare a new variable you need to use `var`, regardless of the type of data you are saving. For example:

```javascript
var firstName = "Adam";
```

We can then check if a variable has been created using `console.log()` and checking the console tool in the developer tools for a browser. For instance, the following code should return 'Adam' in the console of the browser.

```javascript
var firstName = "Adam";
console.log(firstName);
```

Similarly, the following code will return '2'.

```javascript
var add = 1+1;
console.log(add);
```

Even arrays, functions and objects use the same var syntax. We'll explore this in more detail later.

#### string.replace()
We can use the `.replace()` function to replace specified strings within a string variable we are interested in. The following provides and example:

```javascript
var titleTemplate = "Title: articleTitle";
var paperTitle = titleTemplate.replace("articleTitle", "The effects of land clearing on rodent populations");

console.log(titleTemplate);
console.log(paperTitle);
```

#### Add New Data to Your HTML Page
The helper.js file contains several pre-formatted variables with data placeholders, %data%. We want to change the data place holders with our real data.

A simple way to change and then add data to specific pre-formatted variables is to:
1. Identify the variable and the data within it you want to change and what you want to change the data too.
2. Create a new variable by replacing the data placeholder with the required data, e.g. `pre-formattedVariable.replace("%data%", newData)`
3. Then append the new variable to the appropriate element within the HTML document, e.g. `$("#header").append(newVar);`

The following data changes the HTMLheaderName and HTMLheaderRole to include data true for me:

```javascript
var firstName = "Adam";
var lastName = "Cardilini";

var formattedName = HTMLheaderName.replace("%data%", firstName + " " + lastName);
var formattedRole = HTMLheaderRole.replace("%data%", "Associate Lecturer");

$("#header").append(formattedRole);
$("#header").prepend(formattedName);

console.log(formattedName);
console.log(formattedRole);
```

You may have noticed that we use `.prepend()` for addomg the new variables. That's because `.append()` only adds things to the end of an element and we wanted to add our name and role to the beginning of the `#header` element. We can add variables to the beginning of an element by using `.prepend()`.

The order is also important with role first then name, because `.prepend()` will add variables to the beginning of an element in the order that they are coded. This means that formattedName, which is added later, actually is prepended in front of formattedRole.

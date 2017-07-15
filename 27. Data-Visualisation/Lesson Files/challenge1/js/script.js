// Establishing a body variable to add elements
var body = d3.selectAll("body");

body.append("p").text("I Love Data")

// Establish a myDiv variable to append <div> in page
var myDiv = d3.select("div");

// Appending data inside the div
myDiv.append("p").text("Paragraph inside a div");

// Adding styling to the div
myDiv.attr("style", "background-color:#ddd; border:solid 4px black; text-align: center");

// Removing red class
myDiv.classed("red", false);
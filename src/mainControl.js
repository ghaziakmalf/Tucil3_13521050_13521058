import * as graph from "./graph.js";


let graph1 = new graph.Graph();
console.log("halo");
graph1.addNode(); // node 0
graph1.addNode(); // node 1
graph1.addNode(); // node 2

graph1.addEdge(0, 1, 10);
graph1.addEdge(0, 2, 5);

graph1.print();

console.log("halo");
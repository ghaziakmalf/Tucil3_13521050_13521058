
/*
    Graph with nodes and neff attributes.
    neff = amount of nodes in the graph
    nodes = array of maps and each map represent a node

    Map is list of pair, each pair consist of keys and value.
    Each pair in the Map are a child node with key = child node name
    and value = distance.

    Naming Constraint:
        - a node name is a number between 0 - (n-1)
        - node name is also the index in array

    further info on js map: https://www.w3schools.com/js/js_maps.asp

    */

export class Graph{
    constructor(){
        this.nodes = [];
        this.neff = 0;
        this.startNode;
        this.finishNode;
    }

    // add empty node without child node
    addNode(){
        this.nodes.push(new Map());
        this.neff++;
    }

    // add edge to node with nodeId to a another node (childNodeId) and distance.
    addEdge(nodeId, childNodeId, distance){
        if(nodeId < this.neff && nodeId >= 0){
            this.nodes[nodeId].set(childNodeId, distance);
        }
        else{
            console.log("addEdge failed, nodeID invalid");
        }
    }

    /*
        print graph to html page with format as below

        for graph:
                0
               / \
              1   2
        
        distance:
            - 0 to 1 = 10
            - 0 to 2 = 5
        
        will print:
        0 = (1,10)(2,5)
        1 =
        2 =
    */
    print(){
        if(this.neff > 0){
            let text = "";
            for (let i = 0; i < this.neff ;i++){
                text += i + " = "; 
                for(let child of this.nodes[i].entries()){
                    text += "("+ child + ")";
                }
                text += "<br>";
            }
            document.getElementById("demo").innerHTML = text;
        }
    }
}

// export function Graph(){
//     this.nodes = [];
//     this.neff = 0;
// };

// // add node with no child
// Graph.prototype.addNode = function(){
//     this.nodes[neff] = new Map();
//     this.neff++;
// }

// Graph.prototype.addEdge = function(nodeId, childNodeId, distance){
//     if(nodeId < this.neff && nodeId >= 0){
//         this.nodes[nodeId].set(childNodeId, distance);
//     }
//     else{
//         console.log("addEdge failed, nodeID invalid");
//     }
// }

// Graph.prototype.print = function(){
//     if(neff > 0){
//         let text = "";
//         for (let i = 0; i < neff ;i++){
//             text += i + " = "; 
//             for(let child of this.nodes[i].entries()){
//                 text += "("+ child + ")";
//             }
//             text += "<br>";
//         }
//         document.getElementById("demo").innerHTML = text;
//     }
// }
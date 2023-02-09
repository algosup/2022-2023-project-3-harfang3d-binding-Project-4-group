open vector2
open vector3
let vector = CreateVector2D(10.0, 0.0)
let vector2 = CreateVector2D(0.0, 0.0)

// get X and Y of vectors 1
printfn "\nGet points of the first vector"
printfn $"The point X= {vector.X} and point Y= {vector.Y}"


//get distance between two vectors
printfn "--------------------------------"
printfn "Distance"
let distance = distanceTo2D (vector, vector2)
let distanceInFs= (distance)
printfn $"The distance is: {distance}"

//Move vector's points
// !!!!!!
//  The first vector is being modified by vectorMovement
// !!!!!!

printfn "--------------------------------"
printfn "Move points"
printfn $"The before movement X= {vector.X} and Y= {vector.Y}"
let move = vectorMovement2D (vector,  -12.0, 36.0)
printfn $"after movement X= {vector.X} and Y= {vector.Y}"

//get midpoint from vector A to B
let Midpoint: Vector2 = midpoint2D (vector, vector2)

printfn "--------------------------------"
printfn "Get mid point"
printfn $"vector X= {vector.X} Y={vector.Y}"
printfn $"vector2 X= {vector2.X} Y={vector2.Y}"
printfn $"The mid point between vector and vector2 is: X= {Midpoint.X} Y: {Midpoint.Y}"

//get percentage of the distance from vector A to B
let percentage: double = percentDistance2D (vector, vector2, 50)
let Newdistance = distanceTo2D (vector, vector2)

printfn "--------------------------------"
printfn "Get percentage between two vectors"
printfn $"vector X= {vector.X} Y={vector.Y}"
printfn $"vector2 X= {vector2.X} Y={vector2.Y}"
printfn $"The distance is: {Newdistance}"
printfn $"The point at 50 percent between vector and vector2 is: {percentage}"
open vector2
open vector2

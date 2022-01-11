size(200,200);

pair[] vertices = {
(0,0),
(1,1),
(2,1),
(3,0),
(0,-1),
(1,-2),
(2,-2),
(3,-1),
};

pair[] edges = {
(0,1),(0,2),(0,5),(0,6),
(1,2),(1,3),(1,4),(1,7),
(2,4),(2,5),
(3,5),(3,7),
(4,5),(4,6),
(6,7)
};



for(pair p:vertices){
    dot(p);
}

for(pair p:edges){

    draw(vertices[(int) p.x] -- vertices[(int) p.y]);
}





int a = 0;

label((string) a,vertices[a],W);

a+=1;

label((string) a,vertices[a],N);

a+=1;

label((string) a,vertices[a],N);

a+=1;

label((string) a,vertices[a],E);

a+=1;

label((string) a,vertices[a],W);

a+=1;

label((string) a,vertices[a],S);

a+=1;

label((string) a,vertices[a],S);

a+=1;

label((string) a,vertices[a],E);
size(200,200);

pair[] vertices = {
(0,0),
(1,0),
(2,0),
(0,-1),
(1,-1),
(2,-1)
};

pair[] edges = {
(0,3),(0,4),
(1,2),(1,3),(1,4),
(2,4),
(4,5)
};



for(pair p:vertices){
    dot(p);
}

for(pair p:edges){

    draw(vertices[(int) p.x] -- vertices[(int) p.y]);
}





int a = 0;

label((string) a,vertices[a],N);

a+=1;

label((string) a,vertices[a],N);

a+=1;

label((string) a,vertices[a],N);

a+=1;

label((string) a,vertices[a],S);

a+=1;

label((string) a,vertices[a],S);

a+=1;

label((string) a,vertices[a],S);

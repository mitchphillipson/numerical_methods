size(200,200);

pair[] vertices = {
(0,0),
(1,sqrt(2)),
(2,0),
};

pair[] edges = {
(0,1)
};


real rad = .125;

for(pair p:vertices){
    draw(circle(p,rad));
}


label("$A$",vertices[0]);
label("$B$",vertices[1]);
label("$C$",vertices[2]);

int a = 0;
int b = 1;

real x_offset = 0;
real y_offset = .25;

draw(".15",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],NW,arrow=EndArcArrow,margin=Margin(4,4));


a = 0;
b = 2;

y_offset = .125;

draw(".45",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],N,arrow=EndArcArrow,margin=Margin(4,4));



a = 1;
b = 2;

y_offset = .25;

draw(".75",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],E,arrow=EndArcArrow,margin=Margin(4,4));



a = 1;
b = 0;

y_offset = -.25;

draw(".15",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],SE,arrow=EndArcArrow,margin=Margin(4,4));




a = 2;
b = 0;

y_offset = -.125;


draw(".5",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],S,arrow=EndArcArrow,margin=Margin(4,4));



a = 2;
b = 1;

y_offset = -.25;


draw(".3",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],W,arrow=EndArcArrow,margin=Margin(4,4));









a = 0;
b = 0;


x_offset = -.25;
y_offset = -.25;


draw(".4",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],W,arrow=EndArcArrow,margin=Margin(4,4));



a = 1;
b = 1;


x_offset = 0;
y_offset = .375;


draw(".1",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],N,arrow=EndArcArrow,margin=Margin(4,4));






a = 2;
b = 2;


x_offset = .25;
y_offset = -.25;


draw(".2",vertices[a].. ((vertices[a].x+vertices[b].x)/2+x_offset,(vertices[a].y+vertices[b].y)/2+y_offset) .. vertices[b],SE,arrow=EndArcArrow,margin=Margin(4,4));



























size(200,200);

dot((0,0));

draw((0,0) -- (1,-2));
label("$\ell$",(.5,-1),NE);


draw((0,0)--(0,-2),dashed);
draw(arc((0,0),(0,-2/6),(1/6,-2/6)));
label("$\theta$",(.1,-.4));

fill(circle((1,-2),.25),white);
draw(circle((1,-2),.25));




draw((1,-2)--(1,-3),Arrow);
label("$F_g$",(1,-2.5),E);


draw((1,-2)--(1-.75*cos(atan(1/2)),-2-.75*sin(atan(1/2))),Arrow);
label("$F_R$",(1-.375*cos(atan(1/2)),-2-.375*sin(atan(1/2))),NW);


draw((1-.75*cos(atan(1/2)),-2-.75*sin(atan(1/2)))--(1,-3),dashed);
draw(arc((1,-3),(1,-2.75),(1-.75*cos(atan(1/2)),-2-.75*sin(atan(1/2)))));
label("$\theta$",(.875,-2.7));




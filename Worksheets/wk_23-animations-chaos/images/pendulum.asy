size(200,200);

dot((0,0));

draw((0,0) -- (1,-2));
label("$\ell_1$",(.5,-1),NE);


draw((0,0)--(0,-2),dashed);
draw(arc((0,0),(0,-2/6),(1/6,-2/6)));
label("$\theta_1$",(.15,-.5));

fill(circle((1,-2),.25),white);
draw(circle((1,-2),.25));


dot((1,-2));


draw((2.5,-3) -- (1,-2));
label("$\ell_2$",(1.75,-2.5),NE);


draw((1,-2)--(1,-3),dashed);
draw(arc((1,-2),(1,-2.5),(1.75,-2.5)));
label("$\theta_2$",(1.35,-2.55));

fill(circle((2.5,-3),.25),white);
draw(circle((2.5,-3),.25));

size(200,200,IgnoreAspect);
import graph;





int[] xgrid = {0,1,2,3,4};
int[] ygrid = {0,1,2,3,4};

pen pengrid = mediumgrey + linewidth(.25);

pen ticks = fontsize(6);

for(int p : xgrid){
	pair f(real x){
		return (p,x);
	}
	draw(graph(f,min(ygrid),max(ygrid)),pengrid);
	xtick("$"+ string(p)+"$",p,ticks);
}

for(int p : ygrid){
	real f(real x){
		return p;
	}
	draw(graph(f,min(xgrid),max(xgrid)),pengrid);
	ytick("$"+ string(p)+"$",p,ticks);
}


xaxis(Label("$x$",align=2S),0,5,EndArrow,above=true);
yaxis(Label("$y$",align=2E),0,5,EndArrow,above = true);





real f(real x){
 return x;
}

real g(real x){
 return -x+4;
}



draw(graph(f,0,2));


draw(graph(g,2,4),dashed);













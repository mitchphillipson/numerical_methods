size(200,200,IgnoreAspect);
import graph;





int[] xgrid = {0,1,2,3,4,5,6,7,8,9};
int[] ygrid = {0,1,2,3,4,5,6,7,8,9};

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


xaxis(Label("$x$",align=2S),0,10,EndArrow,above=true);
yaxis(Label("$y$",align=2E),0,10,EndArrow,above = true);





real f(real x){
 return (x+1)*sqrt(1-1/2*sin(x)^2);//sqrt(1-2*x^2)/sqrt(1-x^2);
}



int steps = 8;

for(int p=0;p<steps;++p){

    real midp = (p*8/steps+((p+1)*8/steps))/2;

    path c = (p*8/steps,0)--(p*8/steps,f(midp))--((p+1)*8/steps,f(midp))--((p+1)*8/steps,0)--cycle;

    fill(c,lightgrey);
    draw(c);

}







draw(graph(f,0,8));













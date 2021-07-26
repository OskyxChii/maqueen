class usuario{
    nombre;
    //mutadores
    setNombre(nombre){ this.nombre=nombre;}
    //accesadores
    getNombre(){ return this.nombre;}
    //customer
    imprimir(){
        return ' Nombre:'+this.nombre;
    }
}
<?php

/*                                                 PHP - MYSQL Functions                
*A connection.php file will create the connection to the server database (variable $con should be stated as global)
*/

// DB Query 
function consulta_bd($query) {
    require "connection.php";
    $result = mysqli_query($con,$query);
    return $result;
}

//Insert 
 function insertar($table_name,$data_field){
    $fields = array_keys($data_field);
    $sql="INSERT INTO ".$table_name."(".implode(',', $fields).")  VALUES('".implode("','", $data_field)."')";
    
    return consulta_bd($sql);

}

//Delete
function eliminar($table_name,$campo_id,$id){

    $sql = "DELETE FROM ".$table_name." WHERE ".$campo_id."=".$id."";
    
    return consulta_bd($sql);
}

//Update
function editar($table_name,$datos_campo,$campo_id,$id){
    $sql = "UPDATE ".$table_name." SET ";
    $datos = array();

    foreach($datos_campo as $columna=>$value){
        $datos[] =$columna."="."'".$value."'";
    }
    
    $sql .= implode(',',$datos);
    $sql.=" WHERE ".$campo_id." = ".$id."";
    return consulta_bd($sql); 
}
//Function to find the match with the $campo_id parameter
function seleccion_id($table_name,$nombre1,$campo_id){
    $sql = "SELECT * FROM ".$table_name." WHERE ".$nombre1." = ".$campo_id."";
    $bd=consulta_bd($sql);
    $GLOBALS['row'] = mysqli_fetch_object($bd);

    return $sql;
}

?>

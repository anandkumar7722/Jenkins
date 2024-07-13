//DAY1 of php 

<?php
?>//is a opening tag 
<?php
$i=10;
$j=20;
print($i+$j);//30
print($i-$j);
print($i/$j);
print($i*$j);

?>//end tag
<?php //is short opening tag
$table=11;
$rows=20;
$i=0;
?>
<table>
  <tr>
    <th>mul</th>
    <th>multi</th>
    <th>result</th>
  </tr>
<?
  for($i = 0; $i<$rows; $i++){
   ?>
  <tr>
    <td><?=$table?></td>
    <td><?=$i?></td>
    <td><?=$i*$table?></td>
  </tr>
  <?
  }
  ?>
</table>

<!DOCTYPE html>
<html>
<body>
 
<?php
echo "My first PHP script!";
?>

</body>
</html>

//day 2 of php 
<?php
printf("hello world %s","php");
$new="php";
printf("\nhello world %s",$new);
//single
/* is sample like c \n is new line 
*/
printf($new);
//join the strings
print "\nhello world is" . $new ."is age of";
printf("\nhell0"."jjj".$new);
echo "\nhell0"."jjj".$new;
//boolean
//true or flase 
$corr=true;
$incorr=false;
print("\ntrue var:".$corr."is true");
print("\ncorr is type ".gettype($corr));
print("\ncorr is type ".gettype($incorr));
print("\ncorr is type ".gettype($rows));
print("corr is type ".gettype(999));
print("corr is type ".gettype(999));

if(NULL == 0 and false == NULL and false == 0 ){
  print("\nboth are same");
}
 if(1==(int)true){
  print("23 is true");
 } 
 else{
  print("23 == false");
 }
 //intergers
 $int1=34;//postive
 $int2=-34;//neg
 $int3=014; //12 octal
 print($int3);
 $int4=0xff;//hexa
 print($int4);
$int5=0b1101001001001000100;
print($int5);
//float
$fl=2.434434344344343443434434343344343;
printf("%.3f<br>\n",$fl);
$f2=2.1e9;
printf("%.5f<br>\n",$f2);
$free=555;
print($free);
//unset($free);//free()the memory space in ram
print($free."value is not found");
//arithmetics
//shorthand arithmetics
$num=0;
$num=$num + 1;
print("$num\n");
$num ++;
print("$num\n");

$her = <<<HEREB
    How are you, $num?<br>
    I am fine.<br>
    What to go out tonight?<br>
    Yes, definitely.<br>
    HEREB;
print($her);
$gg = <<<"anand"
    How are you, <br>
    I am fine.<br>
    What to go out tonight?<br>
    Yes, definitely.<br>
    anand;
    print($gg); 




?>
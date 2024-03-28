Loop
{
    if (A_Index > 25) ; Il loop verrà eseguito 25 volte
        {
        break  ; Termine del loop
        }
    if (A_Index < 20)
        {
        continue ; Salta ciò che viene dopo e ricomincia il loop
        }
    MsgBox % A_Index
}
return

While (A_Index < 6) ; Il loop verrà eseguito 5 volte. Parentesi facoltative
{
    MsgBox % A_Index
}

/*
La variabile "A_Index" contiene il numero di volte che il
loop è stato eseguito (parte da 1).
*/
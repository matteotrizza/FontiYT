Gui, Add, Checkbox, vRelativo, Errore relativo
Gui, Add, Checkbox, vSpeed, Velocita'
Gui, Add, Button, Default w80, Ok
Gui, Show, W380 H200, Elaborazione dati | Fisica
return

ButtonOk:
Gui, Submit, NoHide
Gui, Destroy

if (Relativo = 1)
{
    InputBox, Value, Inserisci valore | Errore relativo, Inserisci il valore rilevato:
    if (ErrorLevel)
    {
        ExitApp
    }
    InputBox, Sens, Inserisci sensibilita' | Errore relativo, Inserisci la sensibilita':
    if (ErrorLevel)
    {
        ExitApp
    }
    ans := Sens/Value
    MsgBox % "L'errore relativo e' " . ans
}

if (Speed = 1)
{
    InputBox, Spazio, Inserisci valore | Velocita', Inserisci la differenza di spazio rilevato:
    if (ErrorLevel)
    {
        ExitApp
    }
    InputBox, Tempo, Inserisci valore | Velocita', Inserisci la differenza di tempo:
    if (ErrorLevel)
    {
        ExitApp
    }
    ans := Spazio/Tempo
    MsgBox % "La velocita' ottenuta e' di " . ans . " m/s"
}
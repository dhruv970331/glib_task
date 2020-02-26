CodeMirror.modeURL = mode_url+"%N/%N.js";
myTextarea = document.getElementById("id_code")
var editor = CodeMirror.fromTextArea(myTextarea, {
    // value:"def func():\n",
    readOnly:true,
    lineNumbers: true
    // mode:"python"
});
code_text = $("#id_code").html()
if(code_text){
    editor.setValue(code_text)
}
editor.setOption("mode", mode);
CodeMirror.autoLoadMode(editor, mode);
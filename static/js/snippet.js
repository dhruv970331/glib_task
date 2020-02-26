CodeMirror.modeURL = mode_url + "%N/%N.js";
myTextarea = document.getElementById("id_code")
var editor = CodeMirror.fromTextArea(myTextarea, {
    // value:"def func():\n",
    lineNumbers: true,
    mode: "python"
});
// code_text = $("#id_code").html()
// if(code_text){
//     console.log("-----------")
//     editor.setValue(code_text)
// }
$("#id_language").change(function (e) {
    console.log("this", e.target.value, mode_url)
    language = e.target.value
    editor.setOption("mode", language);
    CodeMirror.autoLoadMode(editor, language);
})

// $("#submit").click(function(e){
//     e.preventDefault()
//     // e.stopPropogation()
//     code = editor.getValue()
//     $("#id_code").html(code)
//     console.log(code,"-------------code")
//     console.log($("#create-form").serialize(),"form")
// })
editor.on("change", function (e) {
    code = e.getValue()
    $("#id_code").html(code)
    if (code) {
        $("#submit").prop("disabled", false)
        return
    }
    $("#submit").prop("disabled", true)
})
// $("#create-form").submit(function(e){
//     e.preventDefault()
//     // e.stopPropogation()
//     console.log($("#create-form").serialize(),"form")
// })

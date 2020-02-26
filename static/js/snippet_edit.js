
    CodeMirror.modeURL = mode_url + "%N/%N.js";
    myTextarea = document.getElementById("id_code")
    config = get_config()
    var editor = CodeMirror.fromTextArea(myTextarea, config);
    code_text = $("#id_code").html()
    if (code_text) {
        editor.setValue(code_text)
    }
    CodeMirror.autoLoadMode(editor, config.mode);
    $("#id_language").change(function (e) {
        console.log("this", e.target.value, mode_url)
        language = e.target.value
        editor.setOption("mode", language);
        CodeMirror.autoLoadMode(editor, language);
    })
    
    editor.on("change", function (e) {
        code = e.getValue()
        $("#id_code").html(code)
        if (code) {
            $("#submit").prop("disabled", false)
            return
        }
        $("#submit").prop("disabled", true)
    })
    
    // $("#id_indent_mode").change(function(e){
    
    // })
function get_config(){
    config = {
        lineNumbers:true,
        mode:mode
    }
    if (indent_mode == "tabs") {
        config.indentWithTabs=true
        config.tabSize=indent_value
        config.indentUnit = indent_value
        return config
    }
    config.indentWithTabs=false
    config.indentUnit = indent_value
    config.tabSize=indent_value
    return config
}
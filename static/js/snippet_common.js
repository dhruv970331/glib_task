$(document).ready(function(){
    $("#id_indent_mode").change(function (e) {
        indent_mode = e.target.value
        indent_value = $("#id_indent_value").val()
        if (indent_mode == "tabs") {
            editor.setOption("indentWithTabs", true)
            editor.setOption("tabSize", indent_value)
            editor.setOption("indentUnit", indent_value)
            return
        }
        editor.setOption("indentWithTabs", false)
        editor.setOption("tabSize", indent_value)
        editor.setOption("indentUnit", indent_value)
    })
    
    $("#id_indent_value").change(function(e){
        indent_value = e.target.value
        indent_mode = $("#id_indent_mode").val()
        if (indent_mode == "tabs") {
            editor.setOption("tabSize", indent_value)
            editor.setOption("indentUnit", indent_value)
            return
        }
        editor.setOption("tabSize", indent_value)
        editor.setOption("indentUnit", indent_value)
    })
})
$(function(){
    
    function save() {
        var source = $('#edit_source').val();
        var commit = $('#commit_msg').val();
        $.ajax({
            url:baseurl+'/save?page='+page+'&lang='+lang+'&commit='+commit,
            data:source,
            type:'POST',
            success:function(msg){
                document.location.reload();
            }
        });
    }
    
    function cancel () {
        document.location.reload();
    }
    
    $('#edit').click(function(){
        var html = '<h1>'+lang+'/'+page+'</h1>';
        html+='<div id="loading"><p style="margin-top:30px;">Loading...one moment</p></div>';
        $('#mainCol').html(html);
        $('#feature').hide();
        $.ajax({
            url:baseurl+'/edit',
            data:{'page':page,'lang':lang},
            success:function(msg){
                html = "<textarea id='edit_source'>"+msg+"</textarea>";
                html+= "<div>Commit message:</div><div><input type='text' value='' id='commit_msg'/></div>";
                html+= "<div style='margin-top:10px;'><button id='save'>Save Changes</button> <button id='cancel'>Cancel Changes</button></div>";
                $('#loading').html(html);
                $('#cancel').click(cancel);
                $('#save').click(save);
            }
        });
        return false;
    });
});

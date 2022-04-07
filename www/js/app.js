eel.config_parse();

eel.expose(config_parse);
function config_parse(path, quality){
    $('#download_path').text(path);
    $('#quality').text(quality);
}
eel.expose(download_status)
function download_status(status){
    switch(status){
        case 'downloading':
            //$('#video-name').text('');
            $('.status-popup .text-block #download-status').text('Загрузка...');
            $('.status-popup').fadeOut('fast');
            $('.status-popup').fadeIn('fast');
            break;
        case 'converting':
            $('.status-popup .text-block #download-status').text('Сведение файлов...');
            break;
        case 'success':
            $('.status-popup .text-block #download-status').text('Загрузка завершена');
            break;
    }
}
eel.expose(name_parse)
function name_parse(name){
    let n = name.substr(0, 30) + '...'
    $('.status-popup .text-block #video-name').text(n);
}
//
function quality_change(quality){
    $('#quality').text(quality);
}
$('#download-button').on('click', function(){
    let url = $('#url').val();
    let quality = $('#quality').text();
    eel.name_parse(url);
    eel.download(url, quality);
});
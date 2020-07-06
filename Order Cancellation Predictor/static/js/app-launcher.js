$(document).ready(function () {
    $('.app-option-toggle').click(function () {
        $('.app-launcher-option-expand').toggleClass('active');
    });
    function getUploadItem(id) {
        return `<div class="mr-3 col-2 h-100 d-flex border file-trigger p-0" data-id='file-section-${id}'>
            <img src="/images/icon-upload.png" class="m-auto icon-upload">
        </div>`;
    }
    function getCarouselItem(id) {
        return `<div class="carousel-item h-100">
            <div class="d-flex h-100 align-items-center">
                ${getUploadItem(id)}
            </div>
        </div>`;
    }
    function addFileSection(id, position) {
        let classPool = ['one', 'two', 'three', 'four', 'five'];
        let html = `
            <div class="d-flex flex-column h-100" id="file-section-${id}">
                <div class="labels d-flex align-items-center">
                    <span class="ey-light-bold pt-20 text-uppercase">Input</span>
                    <span class="ey-light-bold pt-12 ml-auto">( .Docx,PDF,Docx,.exl,ppt)</span>
                </div>
                <div class="upload-section h-100 shape upload-shape ${classPool[position]} d-flex">
                    <div class="inner m-auto">
                        <div class="content">
                            <div class="header d-flex align-items-center">
                                <span class="ey-light pt-14 file-name">Filename.doc(${id})</span>
                                <img class="icon-refresh ml-auto" src="/images/icon-refresh.png">
                                <img class="icon-download" src="/images/icon-download.png">
                            </div>
                            <div
                                class="file-display-container d-none justify-content-center align-items-center">
                                <img class="img-fluid w-75 h-75" src="">
                            </div>
                            <div
                                class="drop-zone-container d-flex justify-content-center align-items-center">
                                <div class="drop-zone d-flex col-6" data-id="${id}">
                                    <form class="w-100" enctype="multipart/form-data">
                                        <input class="d-none" type="file" name="files[]"
                                            id="drop-zone-file" />
                                        <label
                                            class="d-flex flex-column h-100 justify-content-center align-items-center"
                                            for="drop-zone-file">
                                            <img src="/images/icon-upload.png">
                                            <span class="pt-12">Drag files or click to upload</span>
                                        </label>
                                    </form>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        $('.upload-section-container > div').removeClass('d-flex').addClass('d-none');
        $('.upload-section-container').append(html);
    }
    function addUploadItem() {
        let id = $('#file-list-carousel .carousel-item > div > div').length;
        let position = $('#file-list-carousel .carousel-item:last > div > div').length;
        if (position > 0 && position < 5) {
            // append item to last carousel item
            $('#file-list-carousel .carousel-item:last > div').append(getUploadItem(++id));
        } else {
            $('#file-list-carousel .carousel-inner').append(getCarouselItem(++id));
            // add new carousel item
        }
        $('#file-list-carousel .carousel-item').removeClass('active');
        $('#file-list-carousel .carousel-item:last').addClass('active');
        addFileSection(id, position % 5);

    }
    $('.add-more').click(addUploadItem);
    $(document).on('click', '.file-trigger', function () {
        $('.upload-section-container > div').removeClass('d-flex').addClass('d-none');
        let id = $(this).attr('data-id');
        $(`.upload-section-container > div#${id}`).removeClass('d-none').addClass('d-flex');
    });

    // File upload drag/drop section
    let isAdvancedUpload = function () {
        let div = document.createElement('div');
        return (('draggable' in div) || ('ondragstart' in div && 'ondrop' in div)) && 'FormData' in window && 'FileReader' in window;
    }();
    let afterFileUpload = function (id, preview) {
        $(`#file-section-${id} .file-display-container img`).attr('src', preview);
        $(`#file-section-${id} .drop-zone-container`).removeClass('d-flex').addClass('d-none');
        $(`#file-section-${id} .file-display-container`).removeClass('d-none').addClass('d-flex');
        $(`.file-trigger[data-id = file-section-${id}] img`).attr('src', preview).addClass('w-100 h-100');
    }
    let dropZone = $('.drop-zone');

    if (isAdvancedUpload) {
        dropZone.addClass('has-advanced-upload');
        let droppedFiles = false;
        $(document).on('drag dragstart dragend dragover dragenter dragleave drop', '.drop-zone', function (e) {
            e.preventDefault();
            e.stopPropagation();
        }).on('dragover dragenter', '.drop-zone', function () {
            $(this).addClass('is-dragover');
        }).on('dragleave dragend drop', '.drop-zone', function () {
            $(this).removeClass('is-dragover');
        }).on('drop', '.drop-zone', function (e) {
            droppedFiles = e.originalEvent.dataTransfer.files;
            let id = $(this).attr('data-id');
            // NOTE : change the preview file in afterfileupload function call
            afterFileUpload(id, '/images/bg-cards-top.png');
        });
    }
    addUploadItem();
});
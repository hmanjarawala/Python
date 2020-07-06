function removeSelectedCard(value, forward) {
    $(`#selected-card-${value}`).remove();
    if (forward) {
        $(`#ai-filter-options input[value='${value}']`).prop('checked', false);
    }
}
function scale(x) {
    const pool = [480, 768, 992, 1200];
    const baseX = 1366;
    x = x / baseX;
    let s = '';
    for (let newBase of pool) {
        s += newBase + ' : ' + Math.floor(newBase * x) + 'px ,'
    }
    return s;
}
$(document).ready(function () {
    let entityPallete = {
        sense: 'blue',
        intelligence: 'yellow',
        conversations: 'purple',
        vision: 'green'
    }
    function showWizard() {
        $('#post-login-overlay').removeClass('bgimg-none');
        $('#body-display').removeClass('d-none').addClass('d-flex');
    }
    $('#unlock').click(function ($event) {
        $('#post-login-overlay').addClass('bgimg-none');
        $('#unlock, #take-me-home').removeClass('d-flex').addClass('d-none');
        setTimeout(showWizard, 0);
    });
    $('.industry-option').click(function () {
        $(this).toggleClass('active');
        let industriesSelected = $('#industry-options .active').length;
        $('#industry-listing .number-selected').text(`${industriesSelected} selected`);
    });
    $('.function-option-outer').click(function () {
        $(this).toggleClass('active');
        let industriesSelected = $('#function-options .active').length;
        $('#function-listing .number-selected').text(`${industriesSelected} selected`);
    });
    $('#step-1-footer .action-button , #step-1-footer span').click(function () {
        $('#wizard-step-1').removeClass('d-flex').addClass('d-none');
        $('#wizard-step-2').removeClass('d-none').addClass('d-flex');
    });
    $('#step-back').click(function () {
        $('#wizard-step-2').removeClass('d-flex').addClass('d-none');
        $('#wizard-step-1').removeClass('d-none').addClass('d-flex');
    });
    let getMid = function (item, xAxis) {
        let element = $(item);
        if (xAxis) {
            return element.width() / 2;
        } else {
            return element.height() / 2;
        }
    }
    // calculate intermediatePoints traveling along vertices
    let calculateIntermediatePoints = function (vertices) {
        let intermediatePoints = [];
        let factor = 8;
        for (let i = 1; i < vertices.length; i++) {
            let pt0 = vertices[i - 1];
            let pt1 = vertices[i];
            let dx = pt1.x - pt0.x;
            let dy = pt1.y - pt0.y;
            for (let j = 0; j < factor; j++) {
                let x = pt0.x + dx * j / factor;
                let y = pt0.y + dy * j / factor;
                intermediatePoints.push({ x: x, y: y });
            }
            intermediatePoints.push(pt1);
        }
        return (intermediatePoints);
    }
    let linkItems = function (color) {
        let vertices = [];
        let connectorPallete = {
            blue: '#168be4',
            yellow: '#efe056',
            green: '#2db657',
            purple: '#3d0f8a'
        }
        let entity = `.entity.${color}`;
        vertices.push({ x: $('.connector').width(), y: $(entity).position().top + getMid(entity) });
        vertices.push({ x: getMid('.connector', true), y: $(entity).position().top + getMid(entity) });
        entity = `.entity-display.${color}`;
        vertices.push({ x: getMid('.connector', true), y: getMid(entity) });
        vertices.push({ x: 0, y: getMid(entity) });
        // calculate incremental points along the path
        let points = calculateIntermediatePoints(vertices);

        // variable to hold how many frames have elapsed in the animation
        // t represents each waypoint along the path and is incremented in the animation loop
        let t = 1;
        let canvas = document.getElementById("connector-canvas");
        canvas.width = $('.connector').width();
        canvas.height = $('.connector').height();
        let context = canvas.getContext("2d");
        context.strokeStyle = connectorPallete[color];
        context.lineWidth = 2;
        context.beginPath();
        context.moveTo(points[t - 1].x, points[t - 1].y);
        // start the animation
        animate();

        // incrementally draw additional line segments along the path
        function animate() {
            if (t < points.length - 1) { requestAnimationFrame(animate); }
            context.lineTo(points[t].x, points[t].y);
            context.stroke();
            t++;
        }
    };
    $('.cognitive-card-option, .entity').click(function () {

        let selected = entityPallete[$(this).attr('data-entity')];

        $('#wizard-step-2').removeClass('d-flex').addClass('d-none');
        $('#wizard-step-3').removeClass('d-none').addClass('d-flex');

        $('.entity-display.blue, .entity-display.yellow, .entity-display.purple, .entity-display.green').removeClass('d-flex').addClass('d-none');
        $(`.entity-display.${selected}`).removeClass('d-none').addClass('d-flex');

        $('.entity').removeClass('active');
        $(`.entity.${selected}`).addClass('active');
        linkItems(selected);
        $('.connector').removeClass('blue yellow purple green').addClass(selected);
    });
    $('.entity-close-container').click(function () {
        $('#wizard-step-3').removeClass('d-flex').addClass('d-none');
        $('#wizard-step-2').removeClass('d-none').addClass('d-flex');
    });
    $('.navbar-icon-outline').click(function () {
        $(this).siblings().removeClass('active');
        $(this).siblings().find('.menu-panel').removeClass('d-flex').addClass('d-none');
        $(this).find('.menu-panel').toggleClass('d-none d-flex');
        $(this).toggleClass('active');
    });
    $('.menu-panel').click(function (event) {
        event.stopPropagation();
    });
    $('#algo-hub-menu a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show');
    });
    $('#ai-filter-listing .fas').click(function () {
        $('#ai-filter-options-container').toggleClass('minimize');
    });
    $('#ai-filter-options input').change(function () {
        let value = $(this).val();
        let text = $.trim($(this).parent().text());
        if ($(this).is(':checked')) {
            addSelectedOption(text, value);
        } else {
            removeSelectedCard(value);
        }
    });
    $('#ai-solution-filter-clear').click(function () {
        $('#ai-selected-filters').html('');
        $('#ai-filter-options input').prop('checked', false);
    });
    function addSelectedOption(text, value) {
        let html = `
        <div id='selected-card-${value}' class="selected-filter d-flex bg-100 align-items-center">
            <span>${text}</span>
            <i class="fas fa-times" onclick="removeSelectedCard('${value}',true)" data-value='${value}'></i>
        </div>
        `;
        $('#ai-selected-filters').append(html);
    }
    $('#ai-filter-search-input').keyup(function () {
        let query = this.value.toLowerCase();
        $('#ai-filter-options .option-item').each(function () {
            let current = $.trim($(this).text()).toLowerCase();
            if (!current.includes(query)) {
                $(this).removeClass('d-flex').addClass('d-none');
            } else {
                $(this).removeClass('d-none').addClass('d-flex');
            }
        });
    });
    $(".entity-card").click(function () {
        $(this).toggleClass('active');
    });
});
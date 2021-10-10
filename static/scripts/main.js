$(document).ready(function() {
    let num = 0;
    $("#single-button").click(function() {
        num += 1;
        entry = $("#single").clone(true);
        entry.attr('hidden', false);
        temp = entry.children('.item-name');
        temp.attr('name', 'item-name'+num);
        temp.attr('disabled', false);
        temp = entry.children('.percentage');
        temp.attr('name', 'percentage'+num);
        temp.attr('disabled', false);
        entry.insertAfter("form > div:last-child");
    });

    $("#repeated-button").click(function() {
        num += 1;
        entry = $("#repeated").clone(true);
        entry.attr('hidden', false);

        temp = entry.children('.item-name');
        temp.attr('name', 'item-name'+num);
        temp.attr('disabled', false);

        temp = entry.children('.percentage');
        temp.attr('name', 'percentage'+num);
        temp.attr('disabled', false);

        temp = entry.children('.num-items');
        temp.attr('name', 'num-items'+num);
        temp.attr('disabled', false);

        temp = entry.children('.counted-items');
        temp.attr('name', 'counted-items'+num);
        temp.attr('disabled', false);

        entry.insertAfter("form > div:last-child");
    });

    $("#weighted-button").click(function() {
        num += 1;
        entry = $("#weighted").clone(true);
        entry.attr('hidden', false);
        temp = entry.children('.item-name');
        temp.attr('name', 'item-name'+num);
        temp.attr('disabled', false);

        temp = entry.children('.percentage');
        temp.attr('name', 'percentage'+num);
        temp.attr('disabled', false);

        temp = entry.children('.num-items');
        temp.attr('name', 'num-items'+num);
        temp.attr('disabled', false);

        entry.insertAfter("form > div:last-child");
    });
});

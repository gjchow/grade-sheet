$(document).ready(function() {
    let num = 0;
    let courses = 0;
    $(".single-button").click(function() {
        num += 1;
        count = this.id[this.id.length -1]
        entry = $("#single").clone(true);
        entry.attr('hidden', false);

        temp = entry.children('.item-name');
        temp.attr('name', 'item-name'+num);
        temp.attr('disabled', false);

        temp = entry.children('.percentage');
        temp.attr('name', 'percentage'+num);
        temp.attr('disabled', false);

        course = $("#course"+count);
        end = course.children('div').last()
        entry.insertAfter(end);
    });

    $(".repeated-button").click(function() {
        num += 1;
        count = this.id[this.id.length -1]
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

        course = $("#course"+count);
        end = course.children('div').last()
        entry.insertAfter(end);
    });

    $(".weighted-button").click(function() {
        num += 1;
        count = this.id[this.id.length -1]
        entry = $("#weighted").clone(true);
        entry.attr('hidden', false);

        temp = entry.children('.item-name');
        temp.attr('name', 'item-name'+num);
        temp.attr('disabled', false);

        temp = entry.children('.weighted-percentage');
        temp.attr('name', 'weighted-percentage'+num);
        temp.attr('disabled', false);

        temp = entry.children('.num-items');
        temp.attr('name', 'num-items'+num);
        temp.attr('disabled', false);

        course = $("#course"+count);
        end = course.children('div').last()
        entry.insertAfter(end);
    });

    $("#course-button").click(function(){
        console.log(courses)
        if (courses < 10) {
            courses += 1
            course = $("#course").clone(true)
            course.attr('id', 'course'+courses);
            course.attr('hidden', false);

            temp = course.children('.course-name');
            temp.attr('name', 'course-name'+String.fromCharCode(courses + 64));
            temp.attr('disabled', false);

            temp = course.children('.single-button');
            temp.attr('id', 'single-button'+courses);

            temp = course.children('.repeated-button');
            temp.attr('id', 'repeated-button'+courses);

            temp = course.children('.weighted-button');
            temp.attr('id', 'weighted-button'+courses);

            course.insertAfter("form > div:last-child");
        }
    });
});

$(document).ready(function(){
    $(document).on('click', 'a.like-btn', function(){
        var servid;
        var usrid;
        servid = $(this).attr("id");
        usrid = $(this).attr("data-usrid");
        $.get("/salon/like/", {service_id : servid, user_id : usrid});
    });
});

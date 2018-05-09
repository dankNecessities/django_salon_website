$(document).ready(function(){
    $(document).on('click', 'a.serv-like-btn', function(){
        var servid;
        var usrid;
        servid = $(this).attr("id");
        usrid = $(this).attr("data-usrid");
        $.get("/salon/likeservice/", {service_id : servid, user_id : usrid});
    });
});
$(document).ready(function(){
    $(document).on('click', 'a.blog-like-btn', function(){
        var servid;
        var usrid;
        blogid = $(this).attr("id");
        usrid = $(this).attr("data-usrid");
        $.get("/salon/likeblog/", {blog_id : blogid, user_id : usrid});
    });
});

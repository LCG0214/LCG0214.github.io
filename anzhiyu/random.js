var posts=["2024/07/02/JVM入门到实战（一）/","2024/05/25/Java跨Docker容器备份数据库数据/","2024/04/25/SpringCloud微服务之Docker篇/","2024/05/08/使用Docker部署Jenkins/","2024/05/27/内网穿透入门使用/","2024/03/22/易班答题助手使用手册/"];function toRandomPost(){
    pjax.loadUrl('/'+posts[Math.floor(Math.random() * posts.length)]);
  };
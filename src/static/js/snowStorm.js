//snowStorm.js https://github.com/scottschiller/Snowstorm
document.head.appendChild(
  Object.assign(document.createElement("link"), {
    rel: "stylesheet",
    type: "text/css",
    href: "https://cdnjs.cloudflare.com/ajax/libs/Snowstorm/20131208/snowstorm.css",
  })
);
document.head.appendChild(
  Object.assign(document.createElement("script"), {
    src: "https://cdnjs.cloudflare.com/ajax/libs/Snowstorm/20131208/snowstorm-min.js",
    onload: () => {
      snowStorm.start();
      snowStorm.excludeMobile = false;
    },
  })
);

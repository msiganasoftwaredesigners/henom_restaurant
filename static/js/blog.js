document.addEventListener("DOMContentLoaded", function () {
  let page = 1;
  let loading = false;

  function loadBlogPosts() {
    if (loading) return;
    loading = true;

    fetch(`/blog/api/posts/?page=${page}`)
      .then((response) => response.json())
      .then((data) => {
        if (data.results.length === 0) return;

        const container = document.getElementById("blog-gallery");

        data.results.forEach((post) => {
          const div = document.createElement("div");
          div.className = "max-w-md mx-auto bg-white rounded-xl shadow-md overflow-hidden m-4";
          div.innerHTML = `
            <div class="w-full h-64 overflow-hidden rounded-t-md relative">
              <img class="w-full h-full object-cover" src="${post.image}" alt="${post.title}">
            </div>
            <div class="p-8">
              <div class="uppercase tracking-wide text-md text-blue-950 font-semibold">
                <a href="/blog/${post.slug}/">${post.title}</a>
              </div>
              <p class="mt-2 text-gray-500">${post.short_description}</p>
            </div>
          `;
          container.appendChild(div);
        });

        page++;
        loading = false;
      })
      .catch(() => {
        loading = false;
      });
  }

  // Load initial posts
  loadBlogPosts();

  // Infinite scroll
  window.addEventListener("scroll", function () {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 150) {
      loadBlogPosts();
    }
  });
});

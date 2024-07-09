<script setup lang="ts">
import { ref, onMounted } from "vue";
import { Book } from "lucide-vue-next";

const articles = ref([]);

onMounted(async () => {
  // This is a placeholder. You'll need to implement the actual fetching of markdown files.
  articles.value = [
    { title: "Article 1", path: "/content/article1.md" },
    { title: "Article 2", path: "/content/article2.md" },
    { title: "Article 3", path: "/content/article3.md" },
  ];
});
</script>

<template>
  <div class="max-w-4xl mx-auto">
    <h1 class="text-4xl font-bold mb-8">Welcome to My Static Site</h1>
    <p class="text-xl mb-8">
      Explore our collection of articles on various topics.
    </p>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div
        v-for="article in articles"
        :key="article.path"
        class="bg-pastel-200 dark:bg-pastel-800 p-6 rounded-lg shadow-md"
      >
        <Book class="h-8 w-8 mb-4" />
        <h2 class="text-2xl font-semibold mb-2">{{ article.title }}</h2>
        <router-link
          :to="{ name: 'Article', params: { path: article.path } }"
          class="text-pastel-600 dark:text-pastel-400 hover:underline"
        >
          Read More
        </router-link>
      </div>
    </div>
  </div>
</template>

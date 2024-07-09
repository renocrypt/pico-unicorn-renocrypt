<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { marked } from "marked";
import { Skeleton } from "@/components/ui/skeleton";

const route = useRoute();
const content = ref("");
const title = ref("");
const date = ref("");
const isLoading = ref(true);

onMounted(async () => {
  isLoading.value = true;
  try {
    // Fetch the article content
    const contentResponse = await fetch(
      `${import.meta.env.BASE_URL}/content/${route.params.slug}.md`
    );
    const markdown = await contentResponse.text();
    content.value = marked(markdown) as string;

    // Fetch the article metadata
    const metadataResponse = await fetch(
      `${import.meta.env.BASE_URL}/articles.json`
    );
    const articles = await metadataResponse.json();
    const currentArticle = articles.find(
      (article: any) => article.slug === route.params.slug
    );
    if (currentArticle) {
      title.value = currentArticle.title;
      date.value = new Date(currentArticle.date).toLocaleDateString("en-US", {
        year: "numeric",
        month: "long",
        day: "numeric",
      });
    }
  } catch (error) {
    console.error("Failed to fetch article:", error);
    content.value = "<p>Failed to load article.</p>";
  } finally {
    isLoading.value = false;
  }
});
</script>

<template>
  <article class="max-w-3xl mx-auto px-4 py-8">
    <Skeleton v-if="isLoading" class="w-2/3 h-10 mb-4" />
    <h1 v-else class="text-3xl font-bold mb-4">{{ title }}</h1>

    <Skeleton v-if="isLoading" class="w-1/3 h-6 mb-8" />
    <p v-else class="text-sm text-muted-foreground mb-8">{{ date }}</p>

    <div v-if="isLoading" class="space-y-4">
      <Skeleton class="w-full h-4" v-for="n in 5" :key="n" />
    </div>
    <div
      v-else
      class="prose dark:prose-invert max-w-none"
      v-html="content"
    ></div>
  </article>
</template>
```

<script setup lang="ts">
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import { marked } from "marked";

const route = useRoute();
const content = ref("");

const fetchArticle = async (path: string) => {
  try {
    const response = await fetch(path);
    const markdown = await response.text();
    content.value = marked(markdown) as string;
  } catch (error) {
    console.error("Error fetching article:", error);
    content.value = "<p>Error loading article</p>";
  }
};

onMounted(() => {
  fetchArticle(route.params.path as string);
});

watch(
  () => route.params.path,
  (newPath) => {
    fetchArticle(newPath as string);
  }
);
</script>

<template>
  <div class="max-w-3xl mx-auto">
    <div v-html="content" class="prose dark:prose-invert"></div>
  </div>
</template>

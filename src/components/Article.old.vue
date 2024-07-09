<script setup lang="ts">
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import { marked } from "marked";

const route = useRoute();
const content = ref("");

onMounted(async () => {
  try {
    const response = await fetch(`/content/${route.params.slug}.md`);
    const markdown = await response.text();
    content.value = marked(markdown) as string;
  } catch (error) {
    console.error("Failed to fetch article:", error);
    content.value = "<p>Failed to load article.</p>";
  }
});
</script>

<template>
  <div class="prose dark:prose-invert max-w-none">
    <div v-html="content"></div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted, computed } from "vue";
import { X, ChevronRight, Calendar } from "lucide-vue-next";
import { Button } from "@/components/ui/button";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Separator } from "@/components/ui/separator";
import { useRouter } from "vue-router";

interface Article {
  slug: string;
  title: string;
  date: string;
}

const props = defineProps<{
  isOpen: boolean;
}>();

const emit = defineEmits<{
  (e: "close"): void;
}>();

const closeSidebar = () => {
  emit("close");
};

const router = useRouter();
const articles = ref<Article[]>([]);

onMounted(async () => {
  try {
    const response = await fetch(`${import.meta.env.BASE_URL}/articles.json`);
    articles.value = await response.json();
  } catch (error) {
    console.error("Failed to fetch articles:", error);
  }
});

const navigateToArticle = (slug: string) => {
  router.push({ name: "Article", params: { slug } });
  closeSidebar();
};

const formatDate = (dateString: string) => {
  return new Date(dateString).toLocaleDateString("en-US", {
    year: "numeric",
    month: "long",
    day: "numeric",
  });
};

const sortedArticles = computed(() => {
  return [...articles.value].sort(
    (a, b) => new Date(b.date).getTime() - new Date(a.date).getTime()
  );
});
</script>

<template>
  <aside
    :class="{
      'translate-x-0': isOpen,
      '-translate-x-full': !isOpen,
    }"
    class="w-80 bg-background/80 backdrop-blur-sm fixed h-full transition-transform duration-300 ease-in-out z-50 shadow-lg"
  >
    <div class="flex flex-col h-full">
      <div class="flex justify-between items-center p-4">
        <h2 class="text-2xl font-semibold">Articles</h2>
        <Button @click="closeSidebar" variant="ghost" size="icon">
          <X class="h-5 w-5" />
        </Button>
      </div>
      <Separator />
      <ScrollArea class="flex-grow">
        <div class="p-4 space-y-4">
          <div
            v-for="article in sortedArticles"
            :key="article.slug"
            class="group"
          >
            <button
              @click="navigateToArticle(article.slug)"
              class="w-full text-left p-3 rounded-lg transition-colors hover:bg-accent"
            >
              <div class="flex justify-between items-start">
                <div>
                  <h3
                    class="font-medium group-hover:text-primary transition-colors"
                  >
                    {{ article.title }}
                  </h3>
                  <p
                    class="text-sm text-muted-foreground flex items-center mt-1"
                  >
                    <Calendar class="h-3 w-3 mr-1" />
                    {{ formatDate(article.date) }}
                  </p>
                </div>
                <ChevronRight
                  class="h-5 w-5 text-muted-foreground group-hover:text-primary transition-colors"
                />
              </div>
            </button>
            <Separator class="my-2" />
          </div>
        </div>
      </ScrollArea>
    </div>
  </aside>
</template>
```

import { createRouter, createWebHistory } from 'vue-router'
import Home from '@/views/Home.vue'
import Article from '@/views/Article.vue'

const routes = [
    { path: '/', name: 'Home', component: Home },
    { path: '/article/:slug', name: 'Article', component: Article, props: true },
]

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes,
})

export default router
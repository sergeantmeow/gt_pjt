<template>
  <div>
    <h2 style="color: #ff2679;">Community</h2>
    <router-link :to="{ name: 'ArticleCreateView' }" class="btn btn-article-view fw-bold">새 글쓰기</router-link>
    <hr>
    <ArticleList />
  </div>
</template>

<script>
import ArticleList from '@/components/ArticleList'

export default {
  name: 'ArticleView',
  components: {
    ArticleList,
  },
  created() {
    this.getArticles()
  },
  methods: {
    getArticles() {
      this.$store.dispatch('getArticles')     
    }
  }
}
</script>

<style>
.btn-article-view {
  background-color: #261639;
  color: #bfbfbf;
}

.btn-article-view:hover {
  background-color: #7c6891;
}
</style>

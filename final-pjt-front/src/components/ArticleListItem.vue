<template>
  <div class="article-list-container">
    <div class="article-list-title">
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
      <h4>{{ article.title }}</h4>
    </router-link>
    </div>
    <div class="article-list-content">
    <h5>{{ article.username }}</h5>
    <p>{{ formatDateTime(article.created_at) }}</p>
    </div>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleListItem',
  props: {
    article: Object,
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      return `${year}-${month}-${day}`;
    },
  }
}
</script>

<style>
.article-list-title a {
  text-decoration: none;
  color: #ff2679
}

.article-list-title a:hover {
  text-decoration: underline;
  color: #7c6891
}

.article-list-content {
  color: #bfbfbf
}
</style>

<template>
  <div class="article-item-container">
    <div class="article-list-title">
    <router-link :to="{
      name: 'ArticleDetailView',
      params: {id: article.id }}">
      <h4>{{ article.title }}</h4>
    </router-link>
    </div>
    <div class="article-item-content">
      <div class="article-item-info">
      <h5>{{ article.username }}</h5>
      {{ formatDateTime(article.created_at) }}
      </div>
    </div>
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
.article-item-container {
  color: #bfbfbf;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 10px;
  margin-bottom: 10px;
  box-shadow: 0 2px 4px #261639;
  transition: box-shadow 0.3s;
}

.article-item-container:hover {
  box-shadow: 0 4px 6px #bfbfbf;
}

.article-list-title {
  flex-grow: 1;
}

.article-list-title a {
  text-decoration: none;
  color: #ff2679;
  transition: color 0.3s;
}

.article-list-title a:hover {
  color: #7c6891;
}

.article-item-content {
  display: flex;
  align-items: center;
  margin-left: 20px;
}

.article-item-info {
  display: flex;
  flex-direction: column;
  text-align: center;
  margin-left: 10px;
}

.article-item-info h5 {
  margin-bottom: 5px;
}

.article-item-info span {
  color: #888888;
  font-size: 14px;
}

</style>

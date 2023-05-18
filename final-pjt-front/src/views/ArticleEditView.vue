<!-- views/CreateView.vue -->

<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="editArticle">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleEditView',
  data() {
    return {
      title: '',
      content: '',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    }
  },
  created(){
    // 기존 게시글의 내용을 가져와서 데이터에 할당
    this.getArticleDetail();
  },
  methods: {
    getArticleDetail() {
      const articleId = this.$route.params.id;
      axios({
        method: 'get',
        url: `${API_URL}/articles/${articleId}/`,
      })
      .then((res) => {
        const article = res.data;
        this.title = article.title;
        this.content = article.content;
      })
      .catch((err) => {
        console.log(err);
      });
    },
    editArticle() {
      const title = this.title
      const content = this.content

      if (!title) {
        alert('제목 입력해주세요')
        return
      } else if (!content){
        alert('내용 입력해주세요')
        return
      }
      axios({
        method: 'put',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`
        },
        data: { title, content},
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>

</style>

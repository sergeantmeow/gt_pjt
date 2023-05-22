<template>
  <div>
    <h2>제목 : {{ article?.title }}</h2>
    <div v-if="article && article.username">
    <p>작성자 : 
      <router-link :to="{ name: 'OtherProfileView', params: { username: article?.username } }">
      {{ article?.username }}
      </router-link>
    </p>
    </div>  
    <div v-if="article && article.image">
    <img :src="'http://127.0.0.1:8000' + article.image" alt="게시글 이미지" class="image-preview">
    </div>
    <p>내용 : {{ article?.content }}</p>
    <p>좋아요 : {{ article?.like_users.length }}</p>
    <p>작성일 : {{ formatDateTime(article?.created_at) }}</p>
    <p>수정일 :  {{ formatDateTime(article?.updated_at) }}</p>
    <button @click="likeArticle">좋아요</button>
    <div v-if="isAuthor">
    <button @click="editArticle">수정</button>
    <button @click="deleteArticle">삭제</button>
    <hr>
    </div>
    <ArticleComment :articleId="articleId"/>
    <!-- 로그인했을 경우만 댓글 달 수 있게 하기 -->
  </div>
</template>

<script>
import axios from 'axios'
import ArticleComment from '@/components/ArticleComment'
const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleDetailView',
  data() {
    return {
      article: null,
      articleId : '',
    }
  },
  components: {
    ArticleComment,
  },
  created() {
    this.articleId = this.$route.params.id
    this.getArticleDetail()
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
    currentUser(){
      return this.$store.getters.currentUser
    },
    isAuthor() {
      return this.isLogin && this.article?.username === this.currentUser.username
    },
  },
  methods: {
    formatDateTime(dateTime) {
      if (!dateTime) return '';

      const date = new Date(dateTime);
      const year = date.getFullYear();
      const month = (date.getMonth() + 1).toString().padStart(2, '0');
      const day = date.getDate().toString().padStart(2, '0');
      const hours = date.getHours().toString().padStart(2, '0');
      const minutes = date.getMinutes().toString().padStart(2, '0');
      const seconds = date.getSeconds().toString().padStart(2, '0');

      return `${year}-${month}-${day} ${hours}:${minutes}:${seconds}`;
    },
    getArticleDetail() {
      if (this.isLogin) {
        axios({
        method: 'get',
        url: `${API_URL}/articles/${ this.$route.params.id }/`,
        })
        .then((res) => {
          this.article = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      } else {
        alert('로그인이 필요한 페이지입니다...')
        this.$router.push({name: 'LogInView'})
      }
    },
    // 삭제하고 다른 페이지 이동 설정하기
    deleteArticle(){ 
      if (confirm('게시물을 삭제하시겠습니까?')) {
    axios({
      method: 'delete',
      url: `${API_URL}/articles/${ this.$route.params.id }/`
    })
    .then(() => {
      this.$router.push({name: 'ArticleView'})
    })
    .catch((err) => {
      console.log(err)
    })
    }
    },
    editArticle(){
      const params = {
        id: this.article.id,
        title: this.article.title,
        image: this.article.image,
        content: this.article.content
      }
      this.$router.push({name: 'ArticleEditView', params: { id: this.article.id }, query: params })
    },
    likeArticle(){
      axios({
        method: 'post',
        url: `${API_URL}/articles/${this.article.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`
        }
      })
      .then(() => {
        this.getArticleDetail()
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style>
.image-preview {
  max-width: 500px;
  max-height: 500px;
}
</style>

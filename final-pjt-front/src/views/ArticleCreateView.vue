<template>
  <div class="container fw-bold">
    <h2 class="title-mg-ct">게시글 작성</h2>
    <form @submit.prevent="createArticle" class="row justify-content-center mt-4">
      <div class="col-md-6">
        <div class="form-group article-create">
          <label for="title">제목</label>
          <input type="text" id="title" v-model.trim="title" class="form-control">
        </div>
        <div class="form-group article-create">
          <label for="content">내용</label>
          <textarea id="content" rows="10" v-model="content" class="form-control"></textarea>
        </div>
        <div v-if="image" class="mb-3 article-img-create-container">
          <img :src="image" alt="이미지" class="article-img-create img-fluid">
        </div>
        <div class="form-group article-create">
          <label for="image">이미지 선택</label>
          <input type="file" id="image" ref="image" @change="handleImageChange" class="form-control-file">
        </div>
        <div class="article-create submit-button">
          <button type="submit" id="submit" class="btn btn-article-create fw-bold">작성</button>
        </div> 
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      title: '',
      content: '',
      image: '',
    }
  },
  computed:{
    isLogin() {
      return this.$store.getters.isLogin
    },
  },
  methods: {
    createArticle() {
      if (!this.title) {
        alert('제목 입력해주세요')
        return
      } else if (!this.content){
        alert('내용 입력해주세요')
        return
      }

      const formData = new FormData();
      formData.append('title', this.title);
      formData.append('content', this.content);
      if (this.image) {
      formData.append('image', this.$refs.image.files[0]);
      }
      
      axios({
        method: 'post',
        url: `${API_URL}/articles/create/`,
        headers: {
          Authorization: `Token ${this.$store.state.user.token}`,
          'Content-Type' : 'multipart/form-data',
        },
        data: formData,
      })
      .then(() => {
        this.$router.push({name: 'ArticleView'})
      })
      .catch((err) => {
        console.log(err)
      })
    },
    handleImageChange(event) {
      const file = event.target.files[0]
      const reader = new FileReader()

      reader.onload = (e) => {
        this.image = e.target.result
      }

      reader.readAsDataURL(file)
    }
  }
}
</script>

<style>
.article-img-create-container {
  margin-top: 10px;
  max-width: 100%;
}

.article-img-create {
  max-width: 100%;
  max-height: 100%;
  width: auto;
  height: auto;
}

.article-create label {
  margin-top: 0.3rem;
  margin-bottom: 0.1rem;
}

.article-create button {
  margin-top: 10px; 
  margin-bottom: 10px;
}

.btn-article-create {
  background-color: #261639;
  color: #bfbfbf;
}

.btn-article-create:hover {
  background-color: #7c6891;
}

</style>

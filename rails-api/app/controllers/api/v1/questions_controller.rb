class Api::V1::QuestionsController < ApplicationController
  def create
    render json: { answer: 'Mock response from Python AI', confidence: 'medium' }
  end
end

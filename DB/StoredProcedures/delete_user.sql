SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

-- ====================================================
-- Author:      Erick Andres Obregon Fonseca
-- Create date: 5th May 2020
-- Description: Delete an user who matches with UserID
-- ====================================================

CREATE PROCEDURE deleteUser
    @UserID int
AS

BEGIN
    SET NOCOUNT ON;

    DELETE FROM [user] WHERE [user].id_user = @UserID;
END
GO
